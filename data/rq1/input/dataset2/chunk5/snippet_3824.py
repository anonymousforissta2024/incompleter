#Source: https://stackoverflow.com/questions/59150717/typeerror-method-object-is-not-subscriptable-python-django
class QuestionSaveTestCase(TestCase):
    """
        Testing Question.save()
    """

    @patch('qanda.service.elasticsearch.Elasticsearch')
    def test_elasticsearch_upsert_on_save(self, ElasticSearchMock):
        user = User.objects.create(
            username='unittest',
            password='unittest'
        )
        question_title = 'Unit test'
        question_body = 'Some unit test'
        q = Question(title=question_title,
                     question=question_body,
                     user=user)
        q.save()

        self.assertIsNotNone(q.id)
        self.assertTrue(ElasticSearchMock.called)
        mock_client = ElasticSearchMock.return_value
        mock_client.update.assert_called_once_with(
            settings.ES_IDENX,
            id=q.id,
            body={
                'doc': {
                    '_type': 'doc',
                    'text': '{}\n{}'.format(question_title, question_body),
                    'question_body': question_body,
                    'title': question_title,
                    'id': q.id,
                    'created': q.created,
                },
                'doc_as_upsert': True,
            }
        )