; https://stackoverflow.com/questions/4564030/how-can-find-all-functions-and-bounded-symbols-in-an-environment
(display "\n")
(display (environment-parent the-environment))
(display (environment-parent system-global-environment))
(exit)
