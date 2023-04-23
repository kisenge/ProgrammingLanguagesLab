#lang slideshow


;this function uses a lambda anon function to check whether values iterated by filter are
;not divisible into list values, and that they are not equal to that value(trial division)

(define (drop-divisible n lst)           
  (filter (lambda (x) (not(and(equal? (modulo x n) 0)(not(equal? x n)))      ))
          lst)
  )


;this function recursively isolates divisors and calls the drop-divisible function to filter primes
(define (sieve-with divisors candidates)
    ( cond
       [(empty? divisors)candidates]
       [else (sieve-with (rest divisors) (drop-divisible (first divisors)  candidates))]))


;main function being called, it calls seive-with and compares all numbers in a range with the same numbers
(define (lesserPrimes n)
  (sieve-with(range 2 n)(range 2 n))
  )


;function testing
;>(is-divisible 10 5)
;>(drop-divisible 5 (list 5 10 11))
;>(sieve-with (list 5 6 7) (list 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21))

>(lesserPrimes 10)


