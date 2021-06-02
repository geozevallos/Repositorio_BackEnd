#SELECT p.nombre, p.precio, c.nombre AS cat
#FROM mydb.producto AS p
#LEFT JOIN mydb.categoria AS c
#ON p.idcategoria = c.idcategoria


#SELECT p.nombre, p.precio, c.nombre AS cat
#FROM mydb.producto AS p
#INNER JOIN mydb.categoria AS c
#ON p.idcategoria = c.idcategoria

SELECT p.nombre, p.precio, c.nombre AS cat
FROM mydb.producto AS p
RIGHT JOIN mydb.categoria AS c
ON p.idcategoria = c.idcategoria
