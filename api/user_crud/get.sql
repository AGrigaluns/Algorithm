DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_artist_by_id`(IN ARTIST_ID INT)
BEGIN
   SELECT *
   FROM artists
   WHERE ArtistId = ARTIST_ID LIMIT 1;
END$$
DELIMITER ;