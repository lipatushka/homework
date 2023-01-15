# git_tutorial
### Repository for my git trainings
1. [GIT HOW TO](https://githowto.com/ru)

## Hot info
## Init
```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@whatever.com"
git init
```
### Show all config preferences
```
git config --list --show-origin
```

### Graph visualization
In `/home/xuser/.gitconfig`:
```
alias.hist3=log --graph --abbrev-commit --decorate --date=format:"%d-%b-%y %H:%M" --format=format:'%C(bold yellow)%h%C(reset) - %C(bold cyan)%ar%C(reset) %C(bold cyan)%ad%C(reset)''    %C(white)%s%C(reset) %C(dim white)- %an%C(reset)''%C(bold red)%d%C(reset)' --all
```

## other
`git config --global core.editor "vim"` - make vim git editor

`.git/info/exclude`

`.gitignore`

`git <command> --help` - вызов справки по команде

* `git branch -a` - просмотр всех веток (локальных (от клона) и удаленных (от оригинала))

## not indexed

`git checkout -- <file>` - discard changes

`git add <file>` - add for commit

## indexed

`git reset HEAD <file>` - make unstaged
 
## commited
`git revert HEAD` - decline the last commit as a new commit with all undo procedures

on master:\
`git reset <HEAD~n or tag>` - make *tag commit* as the last one as "nothing to commit, working tree is clean". All new commits will form a new branch bypassing childs of *tag commit*. --hard flag also discards the diff (modified, not indexed) formed by this operation. History will only show TAGED child commits of *tag commit* and all intermediate commits. When deleting TAG on child - it and intermediate won't be displayed in history, but will still available owing to its hash.\
Also if there were another branches with younger history - they will display. You must delete them using `git branch -D <branchname>`.

### Подробнее о `git reset`
`git reset --hard <tag>` обрубает дерево в месте тэга, однако обрубленные ветки можно восстановить, если их **концы** протэгированы или если известен их хэш: `git checkout <tag>`. Это создаст **detached HEAD** - фактически безымянная ветка, от которой можно коммититься. При чекауте с безымянной ветки с новыми коммитами на другую ветку (нормальную, с именем) изменения, сделанные на безымянной ветке, не отображаются в дереве, но **сохраняются**. При этом возникает сообщение:
```
Warning: you are leaving 9 commits behind, not connected to
any of your branches:

  0777aad new file5
  85f192d mod 7
  530037f mod 6
  329e905 mod 5
 ... and 5 more.

If you want to keep them by creating a new branch, this may be a good time
to do so with:

 git branch <new-branch-name> 0777aad

Switched to branch 'b4'
```

### Как создать detached HEAD
Нужно просто сделать чекаут на любой тэг, а не на имя ветки:
```
git checkout 85f192d

Note: checking out '85f192d'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at 85f192d mod 7
```
```
git status

HEAD detached at 85f192d
nothing to commit, working tree clean
```

  
`git commit --amend` - add changes into the last commit

### Как устранять detached head
`git checkout -b <branch name>`
или
`git branch <new-branch-name> <hash>`, где `<hash>` - конец ветки

## tags
on branch: `git tag <name>` / `git tag -d <name>`

## merge, merge conflicts
branches: master, slave \
on branch master:
```git merge slave```

conflict:
```
<<<<<<< HEAD
version on branch master
=======
version on branch slave
>>>>>>> b1
```

next:
```
git add .
git commit -m "merge complete"
```

## Клонирование репозитория, `origin`
Копия и оригинал могут храниться где угодно: оригинал - в облаке (GitHub), копия - на локальной машине; или наоборот; или оба на локальной машине. Традиционно оригинальный репозиторий помечается словом `origin`.

При клонировании репозитория командой `git clone` появляются `origin`-ветки:
* Все ветки оригинала (пусть `b1`, `b2`, `master`) в клонированном репозитории будут называться `origin/<branch_name>` (`origin/b1`, `origin/b2`, `master`)
* Также в клоне появится локальный `HEAD` и появится `origin/HEAD`. Локальный `HEAD` будет указывать на единственную вновь созданную локальную ветку (она будет подсвечена зеленым и отображаться командой `git branch` - show local branches). Удаленные ветки можно посмотреть командой `git branch -a`. Они подсвечены красным.`origin/HEAD` указывает на ту удаленную ветку, на которую указывал HEAD в оригинальном репозитории в момент клонирования. 

* `git remote` - посмотреть список всех удаленных / родительских репозиториев (от кого клонировались)
* `git remote show <remote repo name>` - посмотреть подробную информацию о связи клона с оригинальным репозиторием:
  * название оригинального репозитория
  * конфигурация `push`, `pull`
  * связи локальных веток с удаленными и др.

## `git fetch`, `git pull`
### `git fetch`
Команда `git fetch` извлекает изменения оригинального репозитория в клонированный. Рассмотрим на конкретном примере.

1. Сделаем изменения в оригинальном репозитории в ветке b8.
2. Перейдем в клон и вызовем статус:
```
On branch b8
Your branch is up to date with 'origin/b8'.

nothing to commit, working tree clean

```
3. `git fetch`; история покажет новый коммит в удаленной ветке `origin/b8`; `git status` теперь покажет:
```
On branch b8
Your branch is behind 'origin/b8' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)

nothing to commit, working tree clean

```

Таким образом, `git fetch` подтягивает изменения оригинала в клон, но только в удаленные ветки. `git merge` позволит влить изменения в удаленной ветке клонированного репозитория в локальную ветку клонированного репозитория. Влив удаленных изменений в локальные ветки после `git fetch` также делает команда `git pull`. Более того `git pull` = `git fetch` + `git merge`.

Типичные сообщения при этих командах:
```
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0)
Unpacking objects: 100% (3/3), done.
From /home/alexander/GitHub/git_tutorial
   175fdf9..d66fbf2  b8         -> origin/b8
Updating 175fdf9..d66fbf2
Fast-forward
 origin_file2 | 1 +
 1 file changed, 1 insertion(+)

```

## Создание отслеживаемых локальных веток
* `git branch --track <local_branch_name> origin/<remote_branch_name>` - создает локальную ветвь `local_branch_name`, с которой будут работать команды `fetch`, `pull` относительно ветки `remote_branch_name`.
* Если существует `origin/branch` не сущесвтует локальной ветки `branch`, то `git checkout branch` создаст эту локальную ветку с автоматическим отслеживанием `remote/branch`.

## Как отправлять изменения в оригинальный репозиторий
Пусть в клоне создали локальную ветку `test_b`, тогда команда git push origin `test_b` создаст в ориинале ветку `test_b` от того же предка. В клоне при этом появится наравне с локальной веткой ещеи `origin/test_b`. Между `test_b` и `origin/test_b` установится слежка.

## Создание чистого репозитория (облачного репозитория, директоия .git, репозиторий для рассылки)
Пусть есть репозиторий `rep`, его клон - `rep_clone` тогда
```
git clone --bare rep rep.git
cd rep
git remote add shared ../rep.git
cd ../rep_clone
git remote add shared ../rep.git
```
Мы создали чистый репозиторий и сделали его "оригинальным" (удаленным) для `rep` (`git remote`: *shared*), `rep_clone` (`git remote`: *shared*, *origin*).

Как лучше всего заливать изменения в облачный репозиторий:
```
In rep:
git push <remote_rep_name> <branch_name> = git push shared test_b
```
Выкачать изменения можно вот так:
```
In rep_clone:
git pull <repo> [<branch>] = git pull shared
```
Последним шагом нужно настроить отслеживание новых ветвей:
```
In rep_clone
git branch --track shared <local_Branch_in_shared_repo_to_track>
or
git checkout -b <local_Branch_in_shared_repo_to_track> 
```
Второй метод интуитивнее проще, но могут возникнуть проблемы, если удаленный репозиториев несколько, и названии удаленной ветви присутствует в обоих. Первый метод решает эту проблему.
## Экспорт реозитория
```
# (From the work directory)
git daemon --verbose --export-all --base-path=.
```
Ключ `--enable=receive-pack` позволит разрешить `push` **любому, кто склонировал репозиторий - осторожнее!**.\
Теперь будет работать команда
```
git clone git://localhost/some_repo.git some_repo
```

## Использование форк и копирование в пустой репозиторий
* Если целью стоит контрибьютить проект - можно отфоркаться от него, тогда форк будет отображаться в персональном аккаунте. Далее обычный клон и все.
* Если же проект не подразумевает контрибьюта - проще создать пустой репозиторий, затем сделать `git remote add edu <ssh_link>` or `git remote add edu <http+TOKEN>` (первый проще), и затем `git push edu`.
