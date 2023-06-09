import pytest
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from task_manager.tasks.models import Task


@pytest.fixture
def user_data():
    return {
        'username': 'User1',
        'first_name': 'Name1',
        'last_name': 'Surname1',
        'password1': 'Testpass23',
        'password2': 'Testpass23',
    }


@pytest.fixture
def test_user(db):
    test_user = User.objects.create(
        username='User1',
        first_name='Name1',
        last_name='Surname1',
        password='Testpass23',
    )
    return test_user


@pytest.fixture
def authenticated_user(client, test_user):
    client.force_login(test_user)
    return test_user


@pytest.fixture
def new_user_data():
    return {
        'username': 'User2',
        'first_name': 'Name2',
        'last_name': 'Surname2',
        'password1': 'Testpass2023',
        'password2': 'Testpass2023',
    }


@pytest.fixture
def status_data():
    return {'name': 'Status1'}


@pytest.fixture
def test_status(db):
    test_status = Status.objects.create(name='Status1')
    return test_status


@pytest.fixture
def label_data():
    return {'name': 'Label1'}


@pytest.fixture
def test_label(db):
    test_label = Label.objects.create(name='Label1')
    return test_label


@pytest.fixture
def task_data():
    return {
        'name': 'Task1',
        'decription': 'My test task',
        'executor': 2,
        'status': 1,
        'labels': [1],
    }


@pytest.fixture
def executor_for_task():
    executor = User.objects.create(
        username='User2',
        first_name='Name2',
        last_name='Surname2',
        password='Test2023'
    )
    return executor


@pytest.fixture
def task(db, test_user, executor_for_task):
    task = Task.objects.create(
        name='Task1',
        description='My test task',
        creator=test_user,
        executor=executor_for_task,
        status=Status.objects.create(name='Status1'),
    )
    task.tasksandlabels.set([Label.objects.create(name='Label1')])
    return task
