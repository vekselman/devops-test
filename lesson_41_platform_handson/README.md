### 1. Lets encrypt
```bash
kubectl apply -f devops-test/lesson_41_platform_handson/lets_encrypt/letsencrypt_argo.yaml
kubectl delete -f devops-test/lesson_41_platform_handson/lets_encrypt/letsencrypt_argo.yaml
kubectl get issuers
kubectl describe issuer letsencrypt-argocd
```
### 2. Cert
Insatll certmanager
```bash
kubectl apply -f https://github.com/jetstack/cert-manager/releases/download/v1.6.1/cert-manager.yaml
```
```bash
kubectl apply -f devops-test/lesson_41_platform_handson/cert/clusterissuer.yaml
kubectl apply -f devops-test/lesson_41_platform_handson/cert/certificate.yaml
kubectl delete -f devops-test/lesson_41_platform_handson/cert/clusterissuer.yaml
kubectl delete -f devops-test/lesson_41_platform_handson/cert/certificate.yaml
```
### 3. ArgoCD
```bash
kubectl create namespace argocd
kubectl config set-context --current --namespace=argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl get all -n argocd
kubectl apply -f devops-test/lesson_41_platform_handson/argocd/argocd_ingress.yaml
kubectl delete -f devops-test/lesson_41_platform_handson/argocd/argocd_ingress.yaml
```
```bash
kubectl edit deployment argocd-server

spec:
  template:
    spec:
      containers:
      - name: argocd-server
        command:
        - argocd-server
        - --repo-server
        - argocd-repo-server:8081
        - --insecure
```
Certs
```bash
```
Password
```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```
Uninstall
```bash
kubectl delete -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```
### HELM
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install argo-cd bitnami/argo-cd
helm install argo-cd bitnami/argo-cd -f devops-test/lesson_41_platform_handson/argocd/argo_helm_values.yaml
```

```bash
helm repo add argo-cd https://argoproj.github.io/argo-helm
helm dep update charts/argo-cd/
helm dep update devops-test/lesson_41_platform_handson/argocd/helm/charts/argo-cd/
```