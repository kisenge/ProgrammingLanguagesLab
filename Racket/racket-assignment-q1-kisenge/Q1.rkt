#lang slideshow


(define (my-rainbow x y)
  (hc-append(hc-append (colorize x "red") (colorize y "yellow") ) (hc-append (colorize x "orange") (colorize y "blue")) (hc-append (colorize x "green") (colorize y "purple")))  
 )



>(my-rainbow (filled-rounded-rectangle 25 25) (arrowhead 25 0))




