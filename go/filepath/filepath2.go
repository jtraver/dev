package main

import (
    "os"
    "path/filepath"
)

func main() {
    filename := "scripts/ls.sh"
    dirname := filepath.Dir(filename)
    os.MkdirAll(dirname, os.ModePerm)
}
