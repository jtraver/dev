package main

import (
    "fmt"
    "os"
    "path/filepath"
)

func main() {
    fmt.Printf("filepath\n")
    logDirContents("..")
    // logDirContents("../..")
}

func logDirContents(dirPath string) {
    logWalkedPaths := filepath.WalkFunc(func(path string, info os.FileInfo, err error) error {
        if err != nil {
            fmt.Printf("stat error for path %q: %s\n", path, err)
            return nil
        }

        if info.IsDir() {
            path = joinTrailingSep(path)
        }

        fmt.Printf("\t%s\n", path)

        return nil
    })

    fmt.Printf("logging directory contents: %q\n", dirPath)

    if err := filepath.Walk(dirPath, logWalkedPaths); err != nil {
        fmt.Printf("ERROR: %s\n", err)
    }
}

func joinTrailingSep(pathElements ...string) string {
    joined := filepath.Join(pathElements...)

    return fmt.Sprintf("%s%c", joined, filepath.Separator)
}
