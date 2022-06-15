#Création de la base

influx;
CREATE DATABASE dbprojet;
USE dbprojet;
INSERT climat,host=temperature value=5;
INSERT climat,host=temperature value=6;
INSERT climat,host=temperature value=7;
INSERT climat,host=temperature value=8;
INSERT climat,host=temperature value=9;
INSERT climat,host=temperature value=24;
INSERT climat,host=temperature value=23.4;
INSERT climat,host=temperature value=23.4;
INSERT climat,host=temperature value=23.4;
INSERT climat,host=temperature value=23.4;
INSERT climat,host=temperature value=23.4;
INSERT climat,host=temperature value=23.4;
INSERT climat,host=temperature value=23.4;
INSERT climat,host=temperature value=23.4;
INSERT climat,host=temperature value=23.4;
INSERT climat,host=temperature value=23.4;
INSERT climat,host=temperature value=23.4;
INSERT climat,host=temperature value=23.4;
INSERT climat,host=temperature value=23.4;
INSERT climat,host=temperature value=23.4;
INSERT climat,host=temperature value=23.4;
exit;
influx auth create --org my-org --all-access;
influx bucket create -n my-bucket -o my-org -r 72h;
