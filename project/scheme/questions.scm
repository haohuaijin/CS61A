(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))


;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
; BEGIN PROBLEM 15
  (define (helper fi li)
    (cond 
      ;((equal? (cdr li) nil) (list (list fi (car li))))
      ((equal? li nil) nil)
      (else 
        (cons 
          (list fi (car li))  ;list和cons的区别和append和extend的区别一样
          (helper (+ fi 1) (cdr li))
          ;(helper (+ fi 1) (cdr li))
        )
      )    
    )
  )
  (helper 0 s)
)
; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
; BEGIN PROBLEM 16
  (cond 
    ((equal? list1 nil) list2)
    ((equal? list2 nil) list1)
    ((comp (car list1) (car list2))
      (cons (car list1) (merge comp (cdr list1) list2))
    )
    (else 
      (cons (car list2) (merge comp (cdr list2) list1))
    )
  )
)
; END PROBLEM 16


(merge < '(1 5 7 9) '(4 8 10))
; expect (1 4 5 7 8 9 10)
(merge > '(9 7 5 1) '(10 8 4 3))
; expect (10 9 8 7 5 4 3 1)

;; Problem 17

(define (nondecreaselist s)
; BEGIN PROBLEM 17
  (define (helper li)
    (cond 
      ((equal? (cdr li) nil) (car li))
      ((> (car li) (cadr li)) (car li)) 
      (else (cons (car li) (helper (cdr li))))
    )
  )


)
; END PROBLEM 17


