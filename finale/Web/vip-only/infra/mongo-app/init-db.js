// Connect to the target database
db = db.getSiblingDB("vipOnlyApp");

// Drop the database to ensure it's clean
db.dropDatabase();

// Create the users collection and any necessary indexes or initial schema setup
db.createCollection("users");

