# helloGit

##Example Full Workflow 

### Navigate to project folder
cd ~/projects/my-github-repo

### Check status (see modified files)
git status

### Stage all changes
git add .

### Commit with message
git commit -m "Update README with installation steps"

### Push to GitHub
git push origin main

**----------------------------------------example full Workflow -----end-----**

## set user.email & user.name 

为什么必须设置？

如果不设置 user.name 和 user.email，首次执行 git commit 时会报错，无法完成提交。
GitHub/GitLab 会通过这个邮箱关联你的账号：只有当提交的邮箱和你 GitHub 账号绑定的邮箱一致时，你的提交记录旁才会显示「已验证」的头像（否则提交会显示为「未知作者」）。
团队协作中，通过提交记录里的邮箱可以快速定位代码修改者，便于沟通和问题追溯。

级别	命令（示例）	作用范围

仓库级	git config user.email "xxx@xx.com"	仅当前仓库生效（覆盖全局）

全局级	git config --global user.email "xxx"	所有仓库生效（默认）

系统级	git config --system user.email "xxx"	电脑上所有用户的仓库生效

可以给工作仓库单独设置工作邮箱，覆盖全局的个人邮箱：
### 进入工作仓库目录

cd ~/projects/company-project

### 设置仅该仓库生效的邮箱

git config user.email "your-work-email@company.com"

### 设置全局邮箱：

git config --global user.email "my-github@example.com"
git config --global user.name "My GitHub Name"

**--------------------------------------------set user.email & user.name -----end ----**

## Rebase 操作示例
### 1. 查看当前分支状态（可选）
git status

### 2. 拉取远程代码并变基
git pull --rebase origin main

### 3. 若出现冲突，修改冲突文件后执行：
git add .  # 标记所有冲突已解决
git rebase --continue  # 继续变基

### 4. 变基完成后，推送本地代码（如果需要）
git push origin main

**--------------------------------------Rebase 示例----**
