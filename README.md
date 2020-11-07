## Avaliação IOT 2

* Abraão Azevedo Oliveira Silva RM83983
* Geovanne Amorim Coelho - RM82578
* Iago Monteiro Garcia - RM82448
* Rodrigo Sussumu Tanaka - RM83888

InfluxDB-name : smart_garden

* curl test true
- curl -H "Content-Type: application/json" \
    -d '{"soil_humidity": 900, "luminosidade": 600, "air_humidity": "45%", "air_temp": "23"}' \
    http://127.0.0.1/api/v1/metric -v
    
* curl teste false
- curl -H "Content-Type: application/json" \
    -d '{"soil_humidity": 700, "luminosidade": 400, "air_humidity": "45%", "air_temp": "23"}' \
    http://127.0.0.1/api/v1/metric -v
