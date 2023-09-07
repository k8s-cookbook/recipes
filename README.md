This is the place where we provide the manifests, scripts, configuration files and other related material used in the [Kubernetes Cookbook](http://shop.oreilly.com/product/0636920064947.do). It's organized along the book's 14 chapters. In bold you see the recipes that contain files, such as YAML manifests, here:

### 1. Getting Started with Kubernetes

- 1.1 Installing the Kubernetes CLI, `kubectl`
- 1.2 Installing Minikube to Run a Local Kubernetes Instance
- 1.3 Using Minikube Locally for Development
- 1.4 Starting Your First Application on Minikube
- 1.5 Local Kubernetes using Kind
- 1.6 Using Kubernetes in Docker Desktop
- 1.7 Switching `kubectl` contexts
- 1.8 An easier way to switch contexts and namespaces

### 2. Creating a Kubernetes Cluster

[Go to resources …](ch02/)

- **2.1 Preparing a new node for Kubernetes Cluster**
- 2.2 Bootstrapping a Kubernetes Control Plane Node
- 2.3 Installing a Container Network Plugin for Cluster Networking
- 2.4 Adding Worker Nodes to a Kubernetes Cluster
- 2.5 Deploying the Kubernetes Dashboard
- **2.6 Accessing the Kubernetes Dashboard**
- 2.7 Deploying the Kubernetes Metrics Server
- 2.8 Downloading a Kubernetes Release from GitHub
- 2.9 Downloading Client and Server Binaries
- 2.10 Using systemd Unit Files for Running Kubernetes Components
- 2.11 Creating a Kubernetes Cluster on Google Kubernetes Engine (GKE)
- 2.12 Creating a Kubernetes Cluster on Azure Kubernetes Service (AKS)
- 2.13 Creating a Kubernetes Cluster on Amazon Elastic Kubernetes Service (EKS)

### 3. Learning to Use the Kubernetes Client

- 3.1 Listing Resources
- 3.2 Deleting Resources
- 3.3 Watching Resource Changes with `kubectl`
- 3.4 Editing objects with `kubectl`
- 3.5 Asking `kubectl` to Explain Resources and Fields

### 4. Creating and Modifying Fundamental Workloads

[Go to resources …](ch04/)

- 4.1 Creating a pod Using `kubectl run`
- 4.2 Creating a Deployment using `kubectl create`
- **4.3 Creating Objects from File Manifests**
- **4.4 Writing a Pod Manifest from Scratch**
- **4.5 Launching a Deployment Using a Manifest**
- 4.6 Updating a Deployment
- **4.7 Running a Batch Job**
- **4.8 Running a Task on a Schedule Within a Pod**
- **4.9 Running Infrastructure Daemons per Node**

### 5. Working with Services

[Go to resources …](ch05/)

- 5.1 Creating a Service to Expose Your Application
- 5.2 Verifying the DNS Entry of a Service
- **5.3 Changing the Type of a Service**
- 5.4 Deploying an Ingress Controller
- **5.5 Making Services Accessible from Outside the Cluster**

### 6. Managing Application Manifests

[Go to resources …](ch06/)

- 6.1 Installing Helm, the Kubernetes Package Manager
- 6.2 Adding Chart Repositories to Helm
- 6.3 Using Helm to Install Applications
- 6.4 Inspecting the Customizable Parameters of a Chart
- 6.5 Overriding Chart Parameters
- 6.6 Getting the User Supplied Parameters of a Helm release
- 6.7 Uninstalling applications with Helm
- 6.8 Creating Your Own Chart to Package Your Application with Helm
- 6.9 Installing Kompose
- 6.10 Converting Your Docker Compose Files to Kubernetes Manifests
- 6.11 Converting Your Docker Compose Files to a Helm Chart
- 6.12 Installing Kapp
- 6.13 **Deploying YAML Manifests using Kapp**

### 7. Exploring the Kubernetes API and Key Metadata

[Go to resources …](ch07/)

- 7.1 Discovering the Kubernetes API Server’s Endpoints
- 7.2 Understanding the Structure of a Kubernetes Manifest
- 7.3 Creating Namespaces to Avoid Name Collisions
- **7.4 Setting Quotas Within a Namespace**
- 7.5 Labeling an Object
- 7.6 Using Labels for Queries
- 7.7 Annotating a Resource with One Command

### 8. Volumes and Configuration Data

[Go to resources …](ch08/)

- **8.1 Exchanging Data Between Containers via a Local Volume**
- **8.2 Passing an API Access Key to a Pod Using a Secret**
- **8.3 Providing Configuration Data to an Application**
- **8.4 Using a Persistent Volume with Minikube**
- **8.5 Understanding Data Persistency on Minikube**
- 8.6 Storing Encrypted Secrets in Version Control

### 9. Scaling

- 9.1 Scaling a Deployment
- 9.2 Using Horizontal Pod Autoscaling
- 9.3 Automatically Resizing a Cluster in GKE
- 9.4 Automatically Resizing a Amazon EKS Cluster

### 10. Security

[Go to resources …](ch10/)

- **10.1 Providing a Unique Identity for an Application**
- **10.2 Listing and Viewing Access Control Information**
- 10.3 Controlling Access to Resources
- **10.4 Securing Pods**

### 11. Monitoring and Logging

[Go to resources …](ch11/)

- 11.1 Accessing the Logs of a Container
- **11.2 Recovering from a Broken State with a Liveness Probe**
- **11.3 Controlling Traffic Flow to a Pod Using a Readiness Probe**
- **11.4 Protecting Slow Starting Containers using Startup Probe**
- **11.5 Adding Liveness and Readiness Probes to Your Deployments**
- 11.6 Accessing Kubernetes Metrics in the CLI
- 11.7 Using Prometheus and Grafana on Minikube

### 12. Maintenance and Troubleshooting

[Go to resources …](ch12/)

- 12.1 Enabling Autocomplete for `kubectl`
- 12.2 Removing a Pod from a Service
- 12.3 Accessing a ClusterIP Service Outside the Cluster
- 12.4 Understanding and Parsing Resource Statuses
- **12.5 Debugging Pods**
- **12.6 Influencing a Pods’ Startup Behavior**
- 12.7 Getting a Detailed Snapshot of the Cluster State
- 12.8 Adding Kubernetes Worker Nodes
- 12.9 Draining Kubernetes Nodes for Maintenance

### 13. Service Mesh

[Go to resources …](ch13/)

- **13.1 Installing the Istio service mesh**
- 13.2 Deploying a microservice with an Istio sidecar
- **13.3 Routing traffic using an Istio virtual service**
- **13.4 Rewriting a URL using an Istio Virtual Service**
- 13.5 Installing the Linkerd service mesh
- 13.6 Deploying a service into the Linkerd mesh
- **13.7 Routing traffic to a service in Linkerd**
- **13.8 Authorizing traffic to the server in Linkerd**

### 14. Serverless and Event Driven Applications

[Go to resources …](ch14/)

- 14.1 Installing the Knative Operator
- **14.2 Installing the Knative Serving**
- 14.3 Installing Knative CLI
- **14.4 Creating a Knative Service**
- **14.5 Installing the Knative Eventing**
- **14.6 Deploying a Knative Eventing Source**
- **14.7 Enabling Knative Eventing Sources**
- **14.8 Installing Event Sources from TriggerMesh**

### 15. Extending Kubernetes

[Go to resources …](ch15/)

- 15.1 Compiling from Source
- 15.2 Compiling a Specific Component
- **15.3 Using a Python Client to Interact with the Kubernetes API**
- **15.4 Extending the API Using Custom Resource Definitions (CRDs)**
