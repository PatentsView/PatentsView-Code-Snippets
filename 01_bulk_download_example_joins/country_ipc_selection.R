# imports
library(fastmatch)
library(dplyr)
library(tidyr)
library(stringr)


# download and unzip relevant files from bulk download site
# for additional file links, see site: https://patentsview.org/download/data-download-tables
ipc_table_url <- "https://s3.amazonaws.com/data.patentsview.org/download/ipcr.tsv.zip"
patent_table_url <- "https://s3.amazonaws.com/data.patentsview.org/download/patent.tsv.zip"
raw_location_table_url <- "https://s3.amazonaws.com/data.patentsview.org/download/rawlocation.tsv.zip"
other_applicant_table_url <- "https://s3.amazonaws.com/data.patentsview.org/download/non_inventor_applicant.tsv.zip"
pat_asgn_url <- "https://s3.amazonaws.com/data.patentsview.org/download/patent_assignee.tsv.zip"
pat_inv_url <- "https://s3.amazonaws.com/data.patentsview.org/download/patent_inventor.tsv.zip"

dl_folder = "Path/To/My/Download/Folder"

for (link in c(ipc_table_url, patent_table_url, raw_location_table_url, other_applicant_table_url, pat_asgn_url, pat_inv_url)) {
  fnam = tail(str_split(link, '/')[[1]], 1)
  download.file(link, paste0(dl_folder,'/',fnam), method = "curl")
  unzip(paste0(dl_folder,'/',fnam), exdir = dl_folder)
}

# faster %in% implementation to speed up repeated use below
# credit: https://stackoverflow.com/questions/32934933/faster-in-operator
`%fin%` <- function(x, table) {  
  stopifnot(require(fastmatch))  
  fmatch(x, table, nomatch = 0L) > 0L
}

#read in files and start filtering
#start with location and build from there
locs <- read.table(file = paste0(dl_folder,'/rawlocation.tsv'), header = T, sep = '\t') %>%
  select(id, location_id, country) %>% #only need id and country columns
  filter(country == "IN") # ISO alpha-2 code for India
# for other country codes, see https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes

# next pick out the inventors, applicants, and assignees who have one of these location ids
invs_in_india <- read.table(file = paste0(dl_folder, '/patent_inventor.tsv'), header = T, sep = '\t', stringsAsFactors = F) %>%
  filter(location_id %fin% locs$location_id)

other_applics_in_india <- read.table(file = paste0(dl_folder, '/non_inventor_applicant.tsv'), header = T, sep = '\t', stringsAsFactors = F) %>%
  select(patent_id, rawlocation_id) %>%
  filter(rawlocation_id %fin% locs$id)

asgns_in_india <- read.table(file = paste0(dl_folder, '/patent_assignee.tsv'), header = T, sep = '\t', stringsAsFactors = F) %>%
  filter(location_id %fin% locs$location_id)

#now we can combine these lists of patents and remove duplicates

country_patlist <- c(invs_in_india$patent_id, asgns_in_india$patent_id, other_applics_in_india$patent_id)
country_patlist <- country_patlist[!duplicated(country_patlist)]

# you can now optionally delete the above data frames to clear up some memory
rm(invs_in_india, other_applics_in_india, asgns_in_india)

# next we'll filter these to the ones with desired IPC codes
good_ipc3 <- c('C07', 'C08', 'C12')
good_ipc4 <- c('A61K', 'A61P', 'C40B')

final_patlist <- read.table(file = paste0(dl_folder,'/ipcr.tsv'), header = T, sep = '\t') %>%
  select(patent_id, section, ipc_class, subclass) %>%
  filter(patent_id %fin% country_patlist) %>%
  mutate(ipc3 = paste0(section,ipc_class), ipc4 = paste0(section,ipc_class,subclass)) %>%
  filter((ipc3 %fin% good_ipc3)|(ipc4 %fin% good_ipc4)) %>%
  select(patent_id)

# this should be a complete list of the patents that match your desired country and IPC codes
# from here you should be able to join any additional tables to get your desired full dataset
# e.g.

mydata <- patlist %>% 
  merge(read.table(file = paste0(dl_folder, '/patent.tsv'), header = T, sep = '\t'), by.x=patent_id, by.y=id, all.x=T)

# and export if desired:
write.csv(mydata, paste0(dl_folder,'/mydata.csv'), row.names = F)