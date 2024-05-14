#Source: https://stackoverflow.com/questions/65940998/airflow-dag-serialization-typeerror-object-of-type-v1pod-is-not-json-seriali
...
volume_task = PythonOperator(
            task_id="task_with_volume",
            python_callable=test_volume_mount,
            executor_config={
                "pod_override": k8s.V1Pod(
                    spec=k8s.V1PodSpec(
                        containers=[
                            k8s.V1Container(
                                name="base",
                                volume_mounts=[
                                    k8s.V1VolumeMount(
                                        mount_path="/foo/", name="example-kubernetes-test-volume"
                                    )
                                ],
                            )
                        ],
                        volumes=[
                            k8s.V1Volume(
                                name="example-kubernetes-test-volume",
                                host_path=k8s.V1HostPathVolumeSource(path="/tmp/"),
                            )
                        ],
                    )
                ),
            },
        )
...