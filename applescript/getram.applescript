on getRam()
    set bytes to system attribute "ram "
    return bytes div (2 ^ 20)
end getRam
display dialog "You have " & getRam() & "MB of RAM.  Wow!"
