from snapshottest.file import FileSnapshot
import time

# Use the database module from our sister repo. We assume it is installed alongside this repo.
import sys
sys.path.insert(1,"../sathunt-database")
import database
import pytest

# Read database config from login.txt
f = open('login.txt', 'r')
lines = f.readlines()
db_name = lines[0].strip()
db_type = lines[1].strip()
endpoint = lines[2].strip()
username = lines[3].strip()
password = lines[4].strip()
f.close()
pytest.db = database.Database(db_name, db_type, endpoint, username, password)

# START IOD cluster search section
def test_find_cluster_simple(snapshot):
    results = pytest.db.findObservationCluster(4376)
    snapshot.assert_match(results)

def test_find_cluster_more_data(snapshot):
    results = pytest.db.findObservationCluster(28888)
    snapshot.assert_match(results)

def test_find_cluster_three(snapshot):
    results = pytest.db.findObservationCluster(4376, minObservationCount=3)
    snapshot.assert_match(results)

def test_find_cluster_two_observers(snapshot):
    results = pytest.db.findObservationCluster(5679, maxMinutesBetweenObservations=90, minObserverCount=2)
    snapshot.assert_match(results)

def test_find_cluster_1_to_15_mins_apart(snapshot):
    results = pytest.db.findObservationCluster(5679, minSecondsBetweenObservations=60, maxMinutesBetweenObservations=15)
    snapshot.assert_match(results)

def test_find_cluster_two_observers_1_to_15_mins_apart(snapshot):
    results = pytest.db.findObservationCluster(5679, minSecondsBetweenObservations=60, minObserverCount=2, maxMinutesBetweenObservations=15)
    snapshot.assert_match(results)
# END IOD cluster search section

# START other query section
def test_find_objects_with_IODs_but_no_TLEs(snapshot):
    results = pytest.db.findObjectsWithIODsButNoTLEs()
    snapshot.assert_match(results)

def test_find_objects_with_IODs_newer_than_TLE(snapshot):
    results = pytest.db.findObjectsWithIODsNewerThanTLE()
    snapshot.assert_match(results)

def test_find_IODs_newer_than_TLEs1(snapshot):
    results = pytest.db.findIODsNewerThanPenultimateTLE(5679)
    snapshot.assert_match(results)

def test_find_IODs_newer_than_TLEs2(snapshot):
    results = pytest.db.findIODsNewerThanPenultimateTLE(11) # Empty result set
    snapshot.assert_match(results)
# END other query section


