import pytest
import pulumi

class mock_bucket(pulumi.runtime.MockResource):
    def new_resource(self, args: pulumi.runtime.MockResourceArgs):
        return [args.name + '_id', args.inputs]
    def call(self, args: pulumi.runtime.MockCallArgs):
        return {}
    
pulumi.runtime.set_mocks(
    mock_bucket(),
    preview=True
)