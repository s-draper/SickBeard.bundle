import re, os, subprocess, string
from base64 import b64encode

####################################################################################################

APPLICATIONS_PREFIX = "/applications/sickbeard"

NAME = 'SickBeard'
ART  = 'art-default.jpg'
ICON = 'icon-default.png'

APIKEY = 'ece5107b40fcee59d9f6a4889a8e0a80'

####################################################################################################

def Start():

    ## make this plugin show up in the 'Applications' section
    ## in Plex. The L() function pulls the string out of the strings
    ## file in the Contents/Strings/ folder in the bundle
    ## see also:
    ##  http://dev.plexapp.com/docs/mod_Plugin.html
    ##  http://dev.plexapp.com/docs/Bundle.html#the-strings-directory
    Plugin.AddPrefixHandler(APPLICATIONS_PREFIX, ApplicationsMainMenu, NAME, ICON, ART)

    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")

    ## set some defaults so that you don't have to
    ## pass these parameters to these object types
    ## every single time
    ## see also:
    ##  http://dev.plexapp.com/docs/Objects.html
    MediaContainer.title1 = NAME
    MediaContainer.viewGroup = "List"
    MediaContainer.art = R(ART)
    DirectoryItem.thumb = R(ICON)
    VideoItem.thumb = R(ICON)
    
    HTTP.CacheTime = CACHE_1HOUR

  


#### the rest of these are user created functions and
#### are not reserved by the plugin framework.
#### see: http://dev.plexapp.com/docs/Functions.html for
#### a list of reserved functions above



#
# Example main menu referenced in the Start() method
# for the 'Applications' prefix handler
#

def ApplicationsMainMenu():

    dir = MediaContainer(viewGroup="InfoList")
    
    dir.Append(
	    Function(
	        DirectoryItem(
                ShowList,
                title="All Shows",
                subtitle="",
                summary="",
                thumb=R(ICON),
                art=R(ART)
            )
        )
    )

    dir.Append(
        Function(
            DirectoryItem(
                ComingEpisodes,
                title="Coming Episodes",
                subtitle="",
                summary="",
                thumb=R(ICON),
                art=R(ART)
            )
        )
    )

    return dir

def ComingEpisodes(sender):

    dir = MediaContainer(viewGroup='InfoList', noCache=True)
 
    return MessageContainer(
        "Not implemented",
        "In real life, you'll make more than one callback,\nand you'll do something useful.\nsender.itemTitle=%s" % sender.itemTitle
    )

  
