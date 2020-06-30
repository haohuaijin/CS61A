;; Scheme ;;

(define (over-or-under a b)
  (cond 
  ((< a b) -1)
  ((> a b) 1)
  (else 0)
  )
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0

(define (filter-lst fn lst)
  (filter fn lst)  
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

(define (make-adder n)
  (lambda (x) (+ n x))
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13

;; Extra questions

(define lst
  (list '(1) 2 '(3 4) 5)
)

(define (composed f g)
  (lambda (x) (f (g x)))
)

(define (remove item lst)
  (filter-lst (lambda (x) (cond ((= x item) 0) (else 1))) lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

(define (no-repeats s)
  (cond
    ((null? s) nil)
    (else
      (cons 
        (car s)
        (no-repeats
          (filter-lst (lambda (x) (cond ((= x (car s)) 0) (else 1))) (cdr s)); method 1
          ;(remove (car s) (cdr s)) method 2
          )
        )
      )
    )
  )

(define (substitute s old new)
  (cond
    ((null? s) nil)
    (else
      (cons
        (cond 
          ((pair? (car s)) (substitute (car s) old new))
          (else (cond ((equal? (car s) old) new) (else (car s))))
        )
        (substitute (cdr s) old new)
      )
    )
  )
)


(define (sub-all s olds news)
  (cond 
    ((null? olds) s)
    (else
      (sub-all 
        (substitute s (car olds) (car news)) 
        (cdr olds) 
        (cdr news)
      )
    )
  )
)