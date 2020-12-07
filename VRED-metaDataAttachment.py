# based on VRED example file examples\snippets\accessAttachments.py 

# please select a node in your scenegraph and execute script.
# open the node editor and scroll to attachments - tagAttachments


# create a name attachment
nameAttachment = createAttachment("TagAttachment")
longStringText1 = "This is my Metadata.\n I can store a long text in here. \n It could be about filename or reference folder etc\n. You can put here whatever you wish"
longStringText2 = "If you want to add more info, just add a new item to the list.\n It can be multiline or singleline.\n This is up to you. :)"
# set the name value of the attachment
vrFieldAccess(nameAttachment).setMString('metaData', [longStringText1,longStringText2 ])
# get the selected node and add the attachment.If a name attachment is already present, it will be replaced
node = getSelectedNode()
node.addAttachment(nameAttachment)


# check if the attachment exists and print the name
if node.hasAttachment('TagAttachment'):
    attachment = node.getAttachment('TagAttachment')
    print(vrFieldAccess(attachment).getMString('metaData'))

