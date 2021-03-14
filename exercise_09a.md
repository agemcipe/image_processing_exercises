## Exercise 09a

We are using the following axioms about openings and closings:
* openings and closings are idempotent
* openings are anti-extensive
* closings are extensive
* openings and closings are increasing

We want to proof that an 'closing-opening' alternate filter an idempotent operation is.
It follows from the axioms above:
```
  closing ( opening ( ) ) = closing ( opening ( ) )

  closing ( opening ( opening ( opening ( ) ) ) ) = closing ( opening ( ) )

  closing ( opening ( closing ( opening ( ) ) ) ) >= closing ( opening ( ) )
```
as well as 
```
  closing ( opening ( ) ) = closing ( opening ( ) )

  closing ( closing ( closing ( opening ( ) ) ) ) = closing ( opening ( ) )

  closing ( opening ( closing ( opening ( ) ) ) ) <= closing ( opening ( ) )
```
and therefore 
```
  closing ( opening ( closing ( opening ( ) ) ) ) = closing ( opening ( ) )
```
which means there filter is an idempotent operation.

