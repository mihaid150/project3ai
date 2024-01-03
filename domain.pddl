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
)
