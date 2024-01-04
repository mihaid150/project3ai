(define
	(domain travellingsalesmancost)
	(:requirements :strips :typing :action-costs)
	(:types
		city
	)
	(:predicates
		(connected ?city1 - city ?city2 - city)
		(current ?city - city)
		(visited ?city - city)
	)
	(:functions
		(distance ?from- - city ?to - city) - number
		(total-cost) - number)

	(:action move
		:parameters (?from- - city ?to - city)
		:precondition (and (current ?from-) (connected ?from- ?to) (not (visited ?to)))
		:effect (and (not (current ?from-)) (current ?to) (visited ?to) (increase (total-cost) (distance ?from- ?to)))
	)
)