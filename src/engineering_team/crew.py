from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class EngineeringTeam:
    """
    EngineeringTeam Crew
    --------------------
    This crew designs, implements, tests, and demos a Python backend
    using a sequential multi-agent workflow.
    """

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ------------------
    # Agents
    # ------------------

    @agent
    def engineering_lead(self) -> Agent:
        """Designs the system and defines module + class structure"""
        return Agent(
            config=self.agents_config['engineering_lead'],
            verbose=True,
        )

    @agent
    def backend_engineer(self) -> Agent:
        """Implements the backend Python module"""
        return Agent(
            config=self.agents_config['backend_engineer'],
            verbose=True,
            allow_code_execution=False,  # IMPORTANT: generate code only
        )

    @agent
    def frontend_engineer(self) -> Agent:
        """Builds a simple Gradio UI to demonstrate the backend"""
        return Agent(
            config=self.agents_config['frontend_engineer'],
            verbose=True,
        )

    @agent
    def test_engineer(self) -> Agent:
        """Writes unit tests for the backend module"""
        return Agent(
            config=self.agents_config['test_engineer'],
            verbose=True,
            allow_code_execution=False,  # IMPORTANT: avoid tool errors
        )

    # ------------------
    # Tasks
    # ------------------

    @task
    def design_task(self) -> Task:
        """High-level design task"""
        return Task(
            config=self.tasks_config['design_task']
        )

    @task
    def code_task(self) -> Task:
        """Backend implementation task"""
        return Task(
            config=self.tasks_config['code_task']
        )

    @task
    def frontend_task(self) -> Task:
        """Frontend (Gradio UI) task"""
        return Task(
            config=self.tasks_config['frontend_task']
        )

    @task
    def test_task(self) -> Task:
        """Unit test generation task"""
        return Task(
            config=self.tasks_config['test_task']
        )

    # ------------------
    # Crew
    # ------------------

    @crew
    def crew(self) -> Crew:
        """Creates and runs the engineering crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
