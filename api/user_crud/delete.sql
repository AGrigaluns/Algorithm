DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_artist_by_id`(IN ARTIST_ID INT)
BEGIN
   DELETE FROM artists
   WHERE ArtistId = ARTIST_ID LIMIT 1;
   commit;
END$$
DELIMITER ;