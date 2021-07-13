-- CREATE:
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_artist`(IN ARTIST_NAME TEXT)
BEGIN
INSERT INTO artists (Name)
VALUE (ARTIST_NAME);
commit;
END$$
DELIMITER ;

-- DELETE:
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_artist_by_id`(IN ARTIST_ID INT)
BEGIN
   DELETE FROM artists
   WHERE ArtistId = ARTIST_ID LIMIT 1;
   commit;
END$$
DELIMITER ;

-- GET:
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_artist_by_id`(IN ARTIST_ID INT)
BEGIN
   SELECT *
   FROM artists
   WHERE ArtistId = ARTIST_ID LIMIT 1;
END$$
DELIMITER ;

-- UPDATE:
ELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_artist_by_id`(IN ARTIST_ID INT, IN NEW_ARTIST_NAME TEXT)
BEGIN
   UPDATE artists
   SET Name = NEW_ARTIST_NAME
   WHERE ArtistId = ARTIST_ID LIMIT 1;
   commit;
END$$
DELIMITER ;