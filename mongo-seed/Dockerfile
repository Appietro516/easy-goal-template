FROM mongo

COPY init.json /init.json
CMD mongoimport --host mongodb --db goals --collection goals_collection --type json --file /init.json --jsonArray

