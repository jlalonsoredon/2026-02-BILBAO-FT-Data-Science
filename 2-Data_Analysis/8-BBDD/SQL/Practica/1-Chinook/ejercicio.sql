--Obtén los clientes de brasil
SELECT FirstName, LastName, Country
FROM customers
WHERE Country LIKE "Brazil";

--Obtén los empleados que son agentes de ventas
SELECT LastName, FirstName, Title
FROM employees
WHERE Title = "Sales Support Agent";

--Obtén las canciones de ‘AC/DC’
SELECT Composer, name
FROM tracks
WHERE Composer = "AC/DC";

--Obtén los campos de los clientes que no sean de USA:Nombrecompleto,ID,País
SELECT CustomerId AS ID, CONCAT(FirstName, " ", LastName) AS "Nombre completo", Country AS Pais
FROM customers
WHERE Country != "USA";

--Obtén los empleados que son agentes de ventas:
--Nombre completo, Dirección(Ciudad,Estado,País) y email
SELECT CONCAT(FirstName, " ", LastName) AS "Nombre completo", CONCAT(City, " | ", State, " | ", Country) AS Dirección, Email
FROM employees
WHERE Title = "Sales Support Agent";

--Obtén una lista con los países no repetidos a los que se han emitido facturas
SELECT DISTINCT BillingCountry
FROM invoices;

--Obtén una lista con los estados de USA no repetidos de donde son los clientes y cuántos clientes en cada uno
SELECT State, count(CustomerId)
FROM customers
GROUP BY State;

--Cuántos artículos tiene la factura 37
SELECT COUNT(InvoiceLineId) AS "Número de lineas de pedido"
FROM invoice_items
WHERE InvoiceId = '37';

--Cuántas canciones tiene ‘AC/DC’
SELECT COUNT(name) AS "Número de canciones"
FROM tracks
WHERE Composer = "AC/DC";

--Cuántos artículos tiene cada factura
SELECT InvoiceId, COUNT(InvoiceLineId) AS "Número de lineas"
FROM invoice_items
GROUP BY InvoiceId;

--Cuántas facturas hay de cada país
SELECT BillingCountry AS PAIS, COUNT(InvoiceId) AS "Número de facturas"
FROM invoices
GROUP BY BillingCountry;

--Cuántas facturas ha habido en 2009 y 2011
SELECT COUNT(InvoiceId) AS "Número de facturas 2009 y 2011"
FROM invoices
WHERE strftime('%Y', InvoiceDate) = '2009' or strftime('%Y', InvoiceDate) = '2011';

--Cuántasfacturashahabidoentre2009y2011
SELECT COUNT(InvoiceId) AS "Número de facturas 2009 y 2011"
FROM invoices
WHERE strftime('%Y', InvoiceDate) >= '2009' AND strftime('%Y', InvoiceDate) <= '2011';
--WHERE strftime('%Y', InvoiceDate) BETWEEN '2009' AND '2011';

--Cuántas clientes hay de España y de Brasil
SELECT Country, COUNT(CustomerId) AS "Número de clientes"
FROM customers
WHERE Country = 'Spain' OR Country ='Brazil'
GROUP BY Country;

--Obtén las canciones que su título empieza por ‘You’
select COUNT(TrackId)
FROM tracks
WHERE Name LIKE "You%";

-------------------------------SEGUNDA PARTE-----------------------------------------------------------------------------
--1. Facturas de Clientes de Brasil, Nombre del cliente, Id de factura, fecha de la factura y el país de la factura
SELECT CONCAT(FirstName, " ", LastName) AS "Nombre completo", fact.InvoiceId, fact.InvoiceDate, fact.BillingCountry
FROM invoices AS fact
    INNER JOIN customers AS cliente ON fact.CustomerId = cliente.CustomerId
WHERE cliente.Country = "Brazil";

--2.Obtén cada factura asociada a cada agente de ventas con su nombrecompleto 
SELECT InvoiceId "ID factura",  
        CONCAT(empleado.FirstName, " ", empleado.LastName) AS "Nombre del agente asociado"
FROM invoices AS fact
    INNER JOIN customers AS cliente ON fact.CustomerId = cliente.CustomerId
    INNER JOIN employees AS empleado ON cliente.SupportRepId = empleado.EmployeeId;

--3.Obtén el nombre del cliente, el país, el nombre del agente y el total
SELECT InvoiceId "ID factura",  
        CONCAT(empleado.FirstName, " ", empleado.LastName) AS "Nombre del agente asociado", 
        CONCAT(cliente.FirstName, " ", cliente.LastName) AS "Nombre del cliente",
        cliente.Country Pais,
        Total
FROM invoices AS fact
    INNER JOIN customers AS cliente ON fact.CustomerId = cliente.CustomerId
    INNER JOIN employees AS empleado ON cliente.SupportRepId = empleado.EmployeeId;
--4.Obtén cada artículo de la factura con el nombre de la canción
SELECT fact.InvoiceId "ID de la factura", cancion.name "Canción", Quantity "Cantidad"
FROM invoices as fact
    INNER JOIN invoice_items AS item ON fact.InvoiceId = item.InvoiceId
    INNER JOIN tracks AS cancion ON item.TrackId = cancion.TrackId
ORDER BY fact.InvoiceId;

--5.Muestra todas las canciones con su nombre, formato, álbum y género
SELECT cancion.Name Canción, media.Name Formato, album.Title Album, genero.Name
FROM tracks AS cancion
    INNER JOIN albums AS album ON cancion.AlbumId = album.AlbumId
    INNER JOIN genres AS genero ON cancion.GenreId = genero.GenreId
    INNER JOIN media_types AS media ON cancion.MediaTypeId = media.MediaTypeId
ORDER BY album.AlbumId;

--6.Cuántas canciones hay en cada playlist
SELECT play.Name "Nombre de la playlist", COUNT(play_tr.TrackId)
FROM playlists AS play
    INNER JOIN playlist_track AS play_tr ON play.PlaylistId = play_tr.PlaylistId
GROUP BY play.PlaylistId;

--7.Cuánto ha vendido cada empleado
SELECT CONCAT(empleado.FirstName, " ", empleado.LastName) AS "Nombre del agente asociado", 
        sum(fact.Total) AS "Total facturado",
        sum(lineas.Quantity) AS "Canciones vendidas"
FROM invoices AS fact
    INNER JOIN customers AS cliente ON fact.CustomerId = cliente.CustomerId
    INNER JOIN employees AS empleado ON cliente.SupportRepId = empleado.EmployeeId
    INNER JOIN invoice_items AS lineas ON fact.InvoiceId = lineas.InvoiceId
GROUP BY empleado.EmployeeId;
--8.¿Quién ha sido el agente de ventas que más ha vendido en 2009?
SELECT CONCAT(empleado.FirstName, " ", empleado.LastName) AS "Nombre del agente asociado", 
        sum(fact.Total) AS "Total facturado"
FROM invoices AS fact
    INNER JOIN customers AS cliente ON fact.CustomerId = cliente.CustomerId
    INNER JOIN employees AS empleado ON cliente.SupportRepId = empleado.EmployeeId
WHERE strftime('%Y', fact.InvoiceDate) >= '2009'
GROUP BY empleado.EmployeeId
ORDER BY sum(fact.Total) DESC
LIMIT 1;

--9.¿Cuáles son los 3 grupos que más han vendido?
SELECT ar.Name "Nombre del grupo", 
        SUM(item.Quantity) "Total ventas"
FROM artists AS ar
    INNER JOIN albums AS al ON ar.ArtistId = al.ArtistId
    INNER JOIN tracks AS tra ON tra.TrackId = tra.TrackId
    INNER JOIN invoice_items AS item ON tra.TrackId = item.TrackId
GROUP BY ar.ArtistId
ORDER BY SUM(item.Quantity) DESC
LIMIT 1;
    