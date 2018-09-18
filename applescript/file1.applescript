set thePath to (path to me as string) & ".myPrefs.scpt"
-- set thePath to (path to me as string) & "Contents:Resources:myPrefs.scpt"
script myPrefs
    property favoriteColor : ""
end script
try
    set myPrefs to load script file thePath
on error
    set favoriteColor of myPrefs to text returned of (display dialog "Favorite Color:" default answer "" buttons {"OK"} default button "OK")
    store script myPrefs in file thePath replacing yes
end try
display dialog "Your favorite color is " & favoriteColor of myPrefs
