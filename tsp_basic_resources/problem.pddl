<<<<<<< Updated upstream
(define (problem problem-1)
    (:domain my_domain)
    (:requirements :strips :typing)
    (:init (not (p2 b c)) (p1 a b c))
    (:goal (p2 b c))
)
=======
(define
	(problem travellingsalesmanbasic)
	(:domain travellingsalesmanbasic)
	(:objects
		TM HD AB SB CJ BH MM - city
	)
	(:init (current TM) (visited TM) (connected TM HD) (connected HD TM) (connected TM BH) (connected BH TM) (connected HD AB) (connected AB HD) (connected AB SB) (connected SB AB) (connected AB CJ) (connected CJ AB) (connected CJ BH) (connected BH CJ) (connected CJ MM) (connected MM CJ) (connected BH MM) (connected MM BH) (connected SB CJ) (connected CJ SB))
	(:goal (and (visited TM) (visited HD) (visited AB) (visited SB) (visited CJ) (visited BH) (visited MM)))
)
>>>>>>> Stashed changes
