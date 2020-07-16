;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;  Call Expressions ;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

scm> (define a (+ 1 2))
scm> a
3

scm> (define b (+ (* 3 3) (* 4 4)))
scm> (+ a b)
28

scm> (= (modulo 10 3) (quotient 5 3))
#t

scm> (even? (+ (- (* 5 4) 3) 2))
#f


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;; Speial Froms ;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; and or not if statement
scm> (if (or #t (/ 1 0)) 1 (/ 1 0))
1

scm> (if (> 4 3) (+ 1 2 3 4) (+ 3 4 (* 3 2)))
10

scm> ((if (< 4 3) + -) 4 100)
-96

scm> (if 0 1 2)
2


; lambda function
; the factorial function
(define 
    (factorial x) 
        (if (= x 1) 
            1 
            (* x (factorial (- x 1)))
        )
)

; the fib number
(define 
    (fib n)
        (if (or (= n 1) (= n 0))
            n
            (+ (fib (- n 2)) (fib (- n 1)))    
        )
)



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;; Pairs and lists ;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (my-append a b)
    (if (equal? nil (cdr a))
        (cons (car a) b)
        (cons (car a) (my-append (cdr a) b))
    )
)



















