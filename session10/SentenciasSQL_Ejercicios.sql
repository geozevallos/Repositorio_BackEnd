#SELECT * FROM mydb.producto
#WHERE nombre LIKE '%a'

#5 productos más caros
#SELECT * FROM mydb.producto
#ORDER BY precio DESC
#LIMIT 5


#VEGATALES PRECIO ENTRE 10 y 12 
#SELECT * FROM mydb.producto
#WHERE idcategoria = 2 AND  precio BETWEEN 10 AND 12

#Cuanto ganaria si vendo todo el stock
SELECT SUM(precio * stock) AS total
 FROM mydb.producto
 
