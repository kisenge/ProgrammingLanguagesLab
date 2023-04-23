#lang slideshow
;(require dyoo-while-loop)

(define input (open-input-file "Q3Input.txt"))






(define (SUM lst)           
  (apply + lst)
  )

(define (funcName)
  ;(print(read input))
 (read input)
  
  )


(define (varNum)
   (print(read input))
   )


;(define (makeListLoop mx)
;   (define lst '())
;
;  (define (loop i)
;    (when (< i mx)
;      ;(define addition(read input))
;      (set! lst
;        (append lst (list(read input)))
;        )
;      ;(print (read input))
;      ;(print mx)
;      ;(print lst)
;      (loop (add1 i))))
;  (loop 0)
;  lst
;
;  (SUM lst)
;  
;
;  
;   )



(define (makeListSum mx)
  ;(print n)
  ;(makeListLoopSum n)
  ;(bigFunc 4)
  (define lst '())

  (define (loop i)
    (when (< i mx)
      ;(define addition(read input))
      (set! lst
        (append lst (list(read input)))
        )
      ;(print (read input))
      ;(print mx)
      ;(print lst)
      (loop (add1 i))))
  (loop 0)
  lst

  (SUM lst)
  
   )





;(define (bigFunc x )
;
;  (let loop([i 0])
;  (if (not(equal? (funcName) 'END ))
;    ;(if (equal? (funcName) 'SUM ) (makeList (read input) )(error "doesn't get here"))
;    ;(if (equal? 1 1 ) (makeList (read input) )(error "doesn't get here"))
;    (cond [(equal? (funcName) 'SUM ) (makeList (read input) )]
;      [(equal? (funcName) 'AVG ) (print 5)]
;      [else 'ok])
;    (print 101 )
;    );if
;    ;(loop ( i))
;   ;(bigFunc 0)
;    )
;  
;  ;(bigFunc 0)
;            
;   )
(define (peek len skp input)
  ;(print(read input))
 (print(peek-string 3 0 input))
 
  
  )

(define (bigFunc x )
  (define (loop i)
;    (define (valCopy)
;      funcName
;      )
  (if (not(equal? (peek-string 3 0 input) "END" ))
    (cond [(equal? (peek-string 3 0 input) "SUM" )
           (begin
             ;(println (peek-string 10 0 input))
             ;(println(read input));nxt line
             (read input);nxt line
      (println(makeListSum (read input) ))
      ;(println (peek-string 3 2 input))
      (loop 5)
      )]
      [(equal? (peek-string 3 2 input) "AVG" )
       (begin
         ;(println (peek-string 3 2 input))
         ;(print(read input));nxt line
         (read input);nxt line
       (println(makeListSum (read input) ))
      (loop 5)
      )]
      [else 'ok])
    
    (print 200)))
(loop 5)
  
            
   )




>(bigFunc 0)
;>(bigFunc 0)


;>(read-string 10 input) ; read first stirng in fil
