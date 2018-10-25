(define (sqrt-iter guess x)
    (if (good-enough? guess x)
        guess
        (sqrt-iter (improve guess x)
                   x)))

(define (improve guess x)
    (average guess (/ x guess)))

(define (average x y)
    (/ (+ x y) 2))

(define (good-enough? guess x)
    (< (abs (- (square guess) x)) 0.0001))

(define (sqrt x)
    (sqrt-iter 1.0 x))

(display "\n")
(display "\n")
(display "sqrt 9\n")
(display (sqrt 9))
(exit)
