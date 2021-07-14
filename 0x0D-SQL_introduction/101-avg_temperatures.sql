-- Display the average temperature by city ordered by temperature (desc)
-- from the temperature table in the hbtn_0c_0 database
SELECT city, AVG(value) as 'avg_temp' FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
