<<<<<<< Updated upstream
(define (domain my_domain)
    (:requirements :strips :typing)
    (:types type_1)
    (:constants a b c - type_1)
    (:predicates (p1 ?x - type_1 ?y - type_1 ?z - type_1)  (p2 ?x - type_1 ?y - type_1))
    (:action action-1
        :parameters (?x - type_1 ?y - type_1 ?z - type_1)
        :precondition (and (p1 ?x ?y ?z) (not (p2 ?y ?z)))
        :effect (p2 ?y ?z)
    )
=======
(define
	(domain travellingsalesmanbasic)
	(:requirements :strips :typing)
	(:types
		city
	)
	(:predicates
		(connected ?city1 - city ?city2 - city)
		(current ?city - city)
		(visited ?city - city)
	)
	(:action move
		:parameters (?from- - city ?to - city)
		:precondition (and (current ?from-) (connected ?from- ?to) (not (visited ?to)))
		:effect (and (not (current ?from-)) (current ?to) (visited ?to))
	)
>>>>>>> Stashed changes
)