# -*- coding: utf-8 -*-

import os
import sys
import json
import tempfile
from unittest import TestCase

from google.appengine.api import apiproxy_stub_map
from google.appengine.api import datastore_file_stub
from google.appengine.api.blobstore import file_blob_storage
from google.appengine.api.blobstore import blobstore_stub
from google.appengine.api.memcache import memcache_stub
from google.appengine.api import user_service_stub

f = open("config.json")
config = json.load(f)
f.close()

GAE_HOME = config["google_app_engine_sdk_home"]
PROJECT_HOME = config["project_home"]
APP_ID = config["app_id"]
AUTH_DOMAIN = config["auth_domain"]
LOGGED_IN_USER = config["logged_in_user"]
EXT_PATH = [
    GAE_HOME,
    PROJECT_HOME,
    os.path.join(GAE_HOME, "google", "appengine", "api"),
    os.path.join(GAE_HOME, "google", "appengine", "ext"),
    os.path.join(GAE_HOME, "lib", "yaml", "lib"),
    os.path.join(GAE_HOME, "lib", "webob"),
]

sys.path = EXT_PATH + sys.path


class GoogleAppEngineTestBase(TestCase):
    def setUp(self):
        os.environ["APPLICATION_ID"] = APP_ID
        os.environ["CURRENT_VERSION_ID"] = "1"
        os.environ["HTTP_HOST"] = "localhost:8080"
        os.environ["AUTH_DOMAIN"] = AUTH_DOMAIN
        os.environ["USER_EMAIL"] = LOGGED_IN_USER

        apiproxy_stub_map.apiproxy = apiproxy_stub_map.APIProxyStubMap()

        self.datastore_path = os.path.join(tempfile.gettempdir(), 'gae_unit.datastore')
        self.blob_storage_path = tempfile.gettempdir()

        self.datastore = datastore_file_stub.DatastoreFileStub(APP_ID, self.datastore_path, None, trusted=True)
        blob_storage = file_blob_storage.FileBlobStorage(self.blob_storage_path, APP_ID)
        self.blobstore = blobstore_stub.BlobstoreServiceStub(blob_storage)
        self.memcache = memcache_stub.MemcacheServiceStub()

        apiproxy_stub_map.apiproxy.RegisterStub('memcache', self.memcache)
        apiproxy_stub_map.apiproxy.RegisterStub('datastore_v3', self.datastore)
        apiproxy_stub_map.apiproxy.RegisterStub('blobstore', self.blobstore)
        apiproxy_stub_map.apiproxy.RegisterStub("user", user_service_stub.UserServiceStub())
