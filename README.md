This is the place where we provide the manifests, scripts, configuration files and other related material used in the [Kubernetes Cookbook](http://shop.oreilly.com/product/0636920064947.do). It's organized along the book's 14 chapters. In bold you see the recipes that contain files, such as YAML manifests, here:

### 1. Getting Started With Kubernetes

- 1.1 Using Kubernetes Without Installation
- 1.2 Installing the Kubernetes CLI `kubectl`
- 1.3 Installing Minikube To Run A Local Kubernetes Instance
- 1.4 Using Minikube Locally for Development
- 1.5 Starting your First Application on Minikube
- 1.6 Accessing the Dashboard in Minikube

### 2. Creating a Kubernetes Cluster

- 2.1 Installing `kubeadm` To Create A Kubernetes Cluster
- 2.2 Bootstrapping A Kubernetes Cluster Using `kubeadm`
- 2.3 Downloading A Kubernetes Release From GitHub
- 2.4 Downloading Client And Server Binaries
- 2.5 Using Hyperkube Image To Run A Kubernetes Master Node With Docker
- 2.6 Writing A Systemd Unit File To Run Kubernetes Components
- 2.7 Creating A Kubernetes Cluster On Google Kubernetes Engine (GKE)
- 2.8 Creating A Kubernetes Cluster On Azure Container Service (ACS)

### 3. Learning to Use the Kubernetes Client

- 3.1 Listing Resources
- 3.2 Deleting Resources
- 3.3 Watching Resource Changes With `kubectl`
- 3.4 Editing Resources With `kubectl`
- 3.5 Letting `kubectl` Explain Resources And Fields

### 4. Creating and Modifying Fundamental Workloads

[Go to resources …](ch04/)

- 4.1 Creating A Deployment Using `kubectl run`
- **4.2 Creating Objects From File Manifests**
- **4.3 Writing A Pod Manifest From Scratch**
- **4.4 Launching Deployment Using A Manifest**
- 4.5 Updating A Deployment

### 5. Working With Services

[Go to resources …](ch05/)

- 5.1 Creating A Service To Expose Your Application
- 5.2 Verifying the DNS Entry of a Service
- **5.3 Changing The Type of a Service**
- 5.4 Deploy An Ingress Controller on Minikube
- **5.5 Making Services Accessible From Outside The Cluster**

### 6. Exploring the Kubernetes API and Key Metadata

[Go to resources …](ch06/)

- 6.1 Discovering API Endpoints Of The Kubernetes API Server
- 6.2 Understanding The Structure Of A Kubernetes Manifest
- 6.3 Creating Namespaces To Avoid Name Collisions
- **6.4 Setting Quotas Within A Namespace**
- 6.5 Labelling An Object
- 6.6 Using Labels For Queries
- 6.7 Annotating a Resource With One Command

### 7. Managing Specialized Workloads

[Go to resources …](ch07/)

- **7.1 Running A Batch Job**
- **7.2 Running a Task on a Schedule Within a Pod**
- **7.3 Running Infrastructure Daemons Per Node**
- **7.4 Managing Stateful and Leader-Follower Apps**
- **7.5 Influencing Pods Startup Behavior**

### 8. Volumes and Configuration Data

[Go to resources …](ch08/)

- **8.1 Exchanging Data Between Containers Via A Local Volume**
- **8.2 Passing An API Access Key To A Pod Using A Secret**
- **8.3 Providing Configuration Data To An Application**
- **8.4 Using A Persistent Volume With Minikube**
- **8.5 Understanding Data Persistency on Minikube**
- 8.6 Dynamically Provision Persistent Storage On GKE

### 9. Scaling

[Go to resources …](ch09/)

- **9.1 Scaling A Deployment**
- 9.2 Automatically Resizing a Cluster in GKE
- 9.3 Automatically Resizing a Cluster in AWS
- 9.4 Using Horizontal Pod Autoscaling on GKE

### 10. Security

[Go to resources …](ch10/)

- 10.1 Providing A Unique Identity For An Application
- 10.2 Listing And Viewing Access Control Information
- 10.3 Controlling Access To Resources
- 10.4 Securing Pods

### 11. Monitoring and Logging

[Go to resources …](ch11/)

- 11.1 Accessing The Logs of a Container
- 11.2 Recover From a Broken State With a Liveness Probe
- 11.3 Control Traffic Flow to a Pod Using a Readiness Probe
- 11.4 Adding Liveness and Readiness Probes To Your Deployments
- 11.5 Enabling Heapster on Minikube To Monitor Resources
- 11.6 Using Prometheus On Minikube
- 11.7 Using Elasticsearch-Fluentd-Kibana (EFK) On Minikube

### 12. Maintenance And Troubleshooting

[Go to resources …](ch12/)

- 12.1 Enabling Autocomplete For `kubectl`
- 12.2 Removing a Pod From a Service
- 12.3 Access a ClusterIP Service Outside the Cluster
- 12.4 Understanding And Parsing Resource Statuses
- 12.5 Debugging Pods
- 12.6 Getting A Detailed Snapshot Of The Cluster State
- 12.7 Adding Kubernetes Worker Nodes
- 12.8 Draining Kubernetes Nodes For Maintenance
- 12.9 Managing `etcd`

### 13. Developing Kubernetes

[Go to resources …](ch13/)

- 13.1 Compiling From Source
- 13.2 Compiling A Specific Component
- 13.3 Using A Python Client To Interact With The Kubernetes API
- 13.4 Extending The API Using Custom Resource Definitions (CRD)

### 14. Ecosystem

- 14.1 Installing Helm, The Kubernetes Package Manager
- 14.2 Using Helm to Install Applications
- 14.3 Creating Your Own Chart To Package Your Application with Helm
- 14.4 Converting Your Docker Compose Files To Kubernetes Manifests
- 14.5 Creating A Kubernetes Cluster With `kubicorn`
- 14.6 Storing Encrypted Secrets in Version Control
- 14.7 Deploying Functions with `kubeless`
