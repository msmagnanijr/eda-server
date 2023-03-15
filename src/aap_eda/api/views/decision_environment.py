#  Copyright 2023 Red Hat, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from django_filters import rest_framework as defaultfilters
from drf_spectacular.utils import (
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)
from rest_framework import status, viewsets
from rest_framework.response import Response

from aap_eda.api import serializers
from aap_eda.core import models


@extend_schema_view(
    list=extend_schema(
        description="List all decision environments",
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                serializers.DecisionEnvironmentSerializer,
                description="Return a list of decision environment.",
            ),
        },
    ),
    retrieve=extend_schema(
        description="Get decision environment by id",
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                serializers.DecisionEnvironmentSerializer,
                description="Return a decision environment by id.",
            ),
        },
    ),
    update=extend_schema(
        description="Update a decision environment",
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                serializers.DecisionEnvironmentSerializer,
                description="Update successful. Return an updated decision environment.",  # noqa: E501
            )
        },
    ),
    partial_update=extend_schema(
        description="Partial update of a decision environment",
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                serializers.DecisionEnvironmentSerializer,
                description="Update successful. Return an updated decision environment.",  # noqa: E501
            )
        },
    ),
    destroy=extend_schema(
        description="Delete a decision environment by id",
        responses={
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                None, description="Delete successful."
            )
        },
    ),
)
class DecisionEnvironmentViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.order_by("id")
    serializer_class = serializers.DecisionEnvironmentSerializer
    filter_backends = (defaultfilters.DjangoFilterBackend,)
    # need to debug why it does not work
    # filterset_class = filters.DecisionEnvironmentFilter  # noqa: E800

    @extend_schema(
        description="Import a decision environment.",
        request=serializers.DecisionEnvironmentCreateSerializer,
        responses={
            status.HTTP_202_ACCEPTED: OpenApiResponse(
                serializers.DecisionEnvironmentSerializer,
                description="Return the new decision environment.",
            ),
        },
    )
    def create(self, request):
        serializer = serializers.DecisionEnvironmentCreateSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        return Response(status=status.HTTP_202_ACCEPTED, data=data)
