from django.test import TestCase
from .models import Projects
from django.urls import reverse
from .forms import ProjectsForm
# Create your tests here.
class ProjectsTest(TestCase):

    # description = models.TextField()

    # url = models.URLField()

    # thumbnail = models.URLField(
    #     blank=True,
    #     null=True
    # )

    # stars = models.PositiveIntegerField(default=0)


    @classmethod
    def setUp(self):
        self.project = Projects.objects.create(
            title="Hallooooo",
            description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum assumenda ducimus corrupti aperiam dolore excepturi, ea quibusdam. Sit ut dolorum ullam accusamus reiciendis nobis possimus qui voluptates cupiditate. Pariatur, aliquid.",
            url="https://www.google.com",
            thumbnail="https://th.bing.com/th/id/OIP.u5o0YZyOoJS2XMtAjuRnWQHaE7?w=200&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
            stars=14
        )
    
    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("landing_page"))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.project.title)
        self.assertContains(response, f'href="/projects/"')
        
    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/experience/")
        
        self.assertEqual(response.status_code, 404)
        
    def test_project_page(self):
        response = self.client.get(reverse("projects"))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")
        self.assertContains(response, self.project.title)

    def test_project_form(self):
        data_form = {
            "title":"Hallooooowww",
            "description":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum assumenda ducimus corrupti aperiam dolore excepturi, ea quibusdam. Sit ut dolorum ullam accusamus reiciendis nobis possimus qui voluptates cupiditate. Pariatur, aliquid.",
            "url":"https://www.google.com",
            "thumbnail":"https://th.bing.com/th/id/OIP.u5o0YZyOoJS2XMtAjuRnWQHaE7?w=200&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
            "stars":20
        }
        form = ProjectsForm(data_form)
        response = self.client.post(
            "/projects/create/",
            data=data_form
        )
        self.assertTrue(form.is_valid)
        self.assertEqual(response.status_code, 302)