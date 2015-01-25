import xbmcaddon

boblight = xbmcaddon.Addon('script.xbmc.boblight')

status = boblight.getSetting('bobdisable')
if status == 'true':
    newstatus = 'false'
else:
    newstatus = 'true'

boblight.setSetting('bobdisable', newstatus)
