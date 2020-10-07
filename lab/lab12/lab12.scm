; Lab 14: Final Review

(define (compose-all funcs)
  (lambda (number)
    (cond 
      ((equal? funcs nil) number)
      (else 
        ((compose-all (cdr funcs)) ((car funcs) number))
      )
    )
  )
)


(define (compose funcs number)
  (cond 
    ((equal? funcs nil) number)
    (else
      (compose (cdr funcs) ((car funcs) number))
    )
  )
)