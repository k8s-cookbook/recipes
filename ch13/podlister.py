#!/usr/bin/env python2

from kubernetes import client, config

config.load_kube_config()
v1 = client.CoreV1Api()
res = v1.list_pod_for_all_namespaces(watch=False)

for pod in res.items:
  print(pod.metadata.name)
