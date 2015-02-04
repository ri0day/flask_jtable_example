DROP TABLE IF EXISTS hostinfov2;
create  virtual table hostinfov2 USING fts4( DT_RowId int(10) NOT NULL auto_increment,hostname varchar(100) UNIQUE,ip text NULL,location text,tags text,hwinfo text,sn varchar(10));

INSERT INTO hostinfov2
		( DT_RowId ,hostname, ip, location, tags, hwinfo, sn )
	VALUES
		( 1,'web01.ejuops.com', '10.0.16.1', 'datacenter', 'webserver', '4c 32g 300g', 'ghs55g' ),
		( 2,'web02.ejuops.com', '10.0.16.2', 'datacenter', 'webserver', '4c 32g 300g', 'ghs65g' ),
		( 3,'web03.ejuops.com', '10.0.16.3', 'datacenter', 'webserver', '4c 32g 300g', 'ghsu5g' ),
		( 4,'web04.ejuops.com', '10.0.16.4', 'datacenter', 'webserver', '4c 32g 300g', 'ghsj5g' ),
		( 5,'web05.ejuops.com', '10.0.16.5', 'datacenter', 'webserver', '4c 32g 300g', 'ghs45u' ),
		( 6,'web06.ejuops.com', '10.0.16.6', 'datacenter', 'webserver', '4c 32g 300g', 'ghs45j' ),
		( 7,'web07.ejuops.com', '10.0.16.7', 'datacenter', 'webserver', '4c 32g 300g', 'ghs4ng' ),
		( 8,'web08.ejuops.com', '10.0.16.8', 'datacenter', 'webserver', '4c 32g 300g', 'ghs44g' ),
		( 9,'web09.ejuops.com', '10.0.16.9', 'datacenter', 'webserver', '4c 32g 300g', 'ggs45g' ),
		( 10,'web10.ejuops.com', '10.0.16.10', 'datacenter', 'webserver', '4c 32g 300g', 'bhs45g' ),
		( 11,'web11.ejuops.com', '10.0.16.11', 'datacenter', 'webserver', '4c 32g 300g', 'nhs45g' ),
		( 12,'web12.ejuops.com', '10.0.16.12', 'datacenter', 'webserver', '4c 32g 300g', 'jhs45g' ),
		( 13,'web13.ejuops.com', '10.0.16.13', 'datacenter', 'webserver', '4c 32g 300g', 'khs45g' ),
		( 14,'web14.ejuops.com', '10.0.16.14', 'datacenter', 'webserver', '4c 32g 300g', 'lhs45g' ),
		( 15,'web15.ejuops.com', '10.0.16.15', 'datacenter', 'webserver', '4c 32g 300g', 'ghs45g' ),
		( 16,'web16.ejuops.com', '10.0.16.16', 'datacenter', 'webserver', '4c 32g 300g', 'ghs45g' ),
		( 17,'web17.ejuops.com', '10.0.16.17', 'datacenter', 'webserver', '4c 32g 300g', 'ghs45g' ),
		( 18,'web18.ejuops.com', '10.0.16.18', 'datacenter', 'webserver', '4c 32g 300g', 'ghs45g' ),
		( 19,'web19.ejuops.com', '10.0.16.19', 'datacenter', 'webserver', '4c 32g 300g', 'ghs45g' ),
		( 20,'web20.ejuops.com', '10.0.16.20', 'datacenter', 'webserver', '4c 32g 300g', 'ghs45g' ),
		( 21,'web21.ejuops.com', '10.0.16.21', 'datacenter', 'webserver', '4c 32g 300g', 'ghs45g' ),
		( 22,'web22.ejuops.com', '10.0.16.22', 'datacenter', 'webserver', '4c 32g 300g', 'ghs45g' ),
		( 23,'web23.ejuops.com', '10.0.16.23', 'datacenter', 'webserver', '4c 32g 300g', 'ghs45g' ),
		( 24,'web24.ejuops.com', '10.0.16.24', 'datacenter', 'webserver', '4c 32g 300g', 'ghs45g' ),
		( 25,'web25.ejuops.com', '10.0.16.25', 'datacenter', 'webserver', '4c 32g 300g', 'ghs45g' ),
		( 26,'web26.ejuops.com', '10.0.16.26', 'datacenter', 'webserver', '4c 32g 300g', 'ghs45g' );
