BACKUP_DIR=/home/dev
DAYS_TO_KEEP=14
DATABASE=tms
USER=dev

FILE="tms_`date +"%Y-%m-%d_%H:%M"`.sql"

OUTPUT_FILE=${BACKUP_DIR}/${FILE}

# do the database backup (dump)
# use this command for a database server on localhost. add other options if need be.
pg_dump -U ${USER} -h localhost ${DATABASE} -a -F p -f ${OUTPUT_FILE}

# gzip the mysql database dump file
gzip $OUTPUT_FILE

# show the user the result
echo "${OUTPUT_FILE}.gz was created:"
ls -l ${OUTPUT_FILE}.gz

# prune old backups
find $BACKUP_DIR -maxdepth 1 -mtime +$DAYS_TO_KEEP -name "*${FILE_SUFFIX}.gz" -exec rm -rf '{}' ';'
