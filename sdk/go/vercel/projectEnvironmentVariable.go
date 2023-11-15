// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vercel

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-vercel/sdk/go/vercel/internal"
)

// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-vercel/sdk/go/vercel"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			exampleProject, err := vercel.NewProject(ctx, "exampleProject", &vercel.ProjectArgs{
//				GitRepository: &vercel.ProjectGitRepositoryArgs{
//					Type: pulumi.String("github"),
//					Repo: pulumi.String("vercel/some-repo"),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = vercel.NewProjectEnvironmentVariable(ctx, "exampleProjectEnvironmentVariable", &vercel.ProjectEnvironmentVariableArgs{
//				ProjectId: exampleProject.ID(),
//				Key:       pulumi.String("foo"),
//				Value:     pulumi.String("bar"),
//				Targets: pulumi.StringArray{
//					pulumi.String("production"),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = vercel.NewProjectEnvironmentVariable(ctx, "exampleGitBranch", &vercel.ProjectEnvironmentVariableArgs{
//				ProjectId: exampleProject.ID(),
//				Key:       pulumi.String("foo"),
//				Value:     pulumi.String("bar-staging"),
//				Targets: pulumi.StringArray{
//					pulumi.String("preview"),
//				},
//				GitBranch: pulumi.String("staging"),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// If importing into a personal account, or with a team configured on the provider, simply use the project_id and environment variable id. - project_id can be found in the project `settings` tab in the Vercel UI. - environment variable id can be taken from the network tab on the project page.
//
// ```sh
//
//	$ pulumi import vercel:index/projectEnvironmentVariable:ProjectEnvironmentVariable example prj_xxxxxxxxxxxxxxxxxxxxxxxxxxxx/FdT2e1E5Of6Cihmt
//
// ```
//
//	Alternatively, you can import via the team_id, project_id and environment variable id. - team_id can be found in the team `settings` tab in the Vercel UI. - project_id can be found in the project `settings` tab in the Vercel UI. - environment variable id can be taken from the network tab on the project page.
//
// ```sh
//
//	$ pulumi import vercel:index/projectEnvironmentVariable:ProjectEnvironmentVariable example team_xxxxxxxxxxxxxxxxxxxxxxxx/prj_xxxxxxxxxxxxxxxxxxxxxxxxxxxx/FdT2e1E5Of6Cihmt
//
// ```
type ProjectEnvironmentVariable struct {
	pulumi.CustomResourceState

	// The git branch of the Environment Variable.
	GitBranch pulumi.StringPtrOutput `pulumi:"gitBranch"`
	// The name of the Environment Variable.
	Key pulumi.StringOutput `pulumi:"key"`
	// The ID of the Vercel project.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
	Targets pulumi.StringArrayOutput `pulumi:"targets"`
	// The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider.
	TeamId pulumi.StringOutput `pulumi:"teamId"`
	// The value of the Environment Variable.
	Value pulumi.StringOutput `pulumi:"value"`
}

// NewProjectEnvironmentVariable registers a new resource with the given unique name, arguments, and options.
func NewProjectEnvironmentVariable(ctx *pulumi.Context,
	name string, args *ProjectEnvironmentVariableArgs, opts ...pulumi.ResourceOption) (*ProjectEnvironmentVariable, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Key == nil {
		return nil, errors.New("invalid value for required argument 'Key'")
	}
	if args.ProjectId == nil {
		return nil, errors.New("invalid value for required argument 'ProjectId'")
	}
	if args.Targets == nil {
		return nil, errors.New("invalid value for required argument 'Targets'")
	}
	if args.Value == nil {
		return nil, errors.New("invalid value for required argument 'Value'")
	}
	if args.Value != nil {
		args.Value = pulumi.ToSecret(args.Value).(pulumi.StringInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"value",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ProjectEnvironmentVariable
	err := ctx.RegisterResource("vercel:index/projectEnvironmentVariable:ProjectEnvironmentVariable", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetProjectEnvironmentVariable gets an existing ProjectEnvironmentVariable resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetProjectEnvironmentVariable(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ProjectEnvironmentVariableState, opts ...pulumi.ResourceOption) (*ProjectEnvironmentVariable, error) {
	var resource ProjectEnvironmentVariable
	err := ctx.ReadResource("vercel:index/projectEnvironmentVariable:ProjectEnvironmentVariable", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ProjectEnvironmentVariable resources.
type projectEnvironmentVariableState struct {
	// The git branch of the Environment Variable.
	GitBranch *string `pulumi:"gitBranch"`
	// The name of the Environment Variable.
	Key *string `pulumi:"key"`
	// The ID of the Vercel project.
	ProjectId *string `pulumi:"projectId"`
	// The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
	Targets []string `pulumi:"targets"`
	// The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider.
	TeamId *string `pulumi:"teamId"`
	// The value of the Environment Variable.
	Value *string `pulumi:"value"`
}

type ProjectEnvironmentVariableState struct {
	// The git branch of the Environment Variable.
	GitBranch pulumi.StringPtrInput
	// The name of the Environment Variable.
	Key pulumi.StringPtrInput
	// The ID of the Vercel project.
	ProjectId pulumi.StringPtrInput
	// The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
	Targets pulumi.StringArrayInput
	// The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider.
	TeamId pulumi.StringPtrInput
	// The value of the Environment Variable.
	Value pulumi.StringPtrInput
}

func (ProjectEnvironmentVariableState) ElementType() reflect.Type {
	return reflect.TypeOf((*projectEnvironmentVariableState)(nil)).Elem()
}

type projectEnvironmentVariableArgs struct {
	// The git branch of the Environment Variable.
	GitBranch *string `pulumi:"gitBranch"`
	// The name of the Environment Variable.
	Key string `pulumi:"key"`
	// The ID of the Vercel project.
	ProjectId string `pulumi:"projectId"`
	// The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
	Targets []string `pulumi:"targets"`
	// The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider.
	TeamId *string `pulumi:"teamId"`
	// The value of the Environment Variable.
	Value string `pulumi:"value"`
}

// The set of arguments for constructing a ProjectEnvironmentVariable resource.
type ProjectEnvironmentVariableArgs struct {
	// The git branch of the Environment Variable.
	GitBranch pulumi.StringPtrInput
	// The name of the Environment Variable.
	Key pulumi.StringInput
	// The ID of the Vercel project.
	ProjectId pulumi.StringInput
	// The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
	Targets pulumi.StringArrayInput
	// The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider.
	TeamId pulumi.StringPtrInput
	// The value of the Environment Variable.
	Value pulumi.StringInput
}

func (ProjectEnvironmentVariableArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*projectEnvironmentVariableArgs)(nil)).Elem()
}

type ProjectEnvironmentVariableInput interface {
	pulumi.Input

	ToProjectEnvironmentVariableOutput() ProjectEnvironmentVariableOutput
	ToProjectEnvironmentVariableOutputWithContext(ctx context.Context) ProjectEnvironmentVariableOutput
}

func (*ProjectEnvironmentVariable) ElementType() reflect.Type {
	return reflect.TypeOf((**ProjectEnvironmentVariable)(nil)).Elem()
}

func (i *ProjectEnvironmentVariable) ToProjectEnvironmentVariableOutput() ProjectEnvironmentVariableOutput {
	return i.ToProjectEnvironmentVariableOutputWithContext(context.Background())
}

func (i *ProjectEnvironmentVariable) ToProjectEnvironmentVariableOutputWithContext(ctx context.Context) ProjectEnvironmentVariableOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProjectEnvironmentVariableOutput)
}

// ProjectEnvironmentVariableArrayInput is an input type that accepts ProjectEnvironmentVariableArray and ProjectEnvironmentVariableArrayOutput values.
// You can construct a concrete instance of `ProjectEnvironmentVariableArrayInput` via:
//
//	ProjectEnvironmentVariableArray{ ProjectEnvironmentVariableArgs{...} }
type ProjectEnvironmentVariableArrayInput interface {
	pulumi.Input

	ToProjectEnvironmentVariableArrayOutput() ProjectEnvironmentVariableArrayOutput
	ToProjectEnvironmentVariableArrayOutputWithContext(context.Context) ProjectEnvironmentVariableArrayOutput
}

type ProjectEnvironmentVariableArray []ProjectEnvironmentVariableInput

func (ProjectEnvironmentVariableArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ProjectEnvironmentVariable)(nil)).Elem()
}

func (i ProjectEnvironmentVariableArray) ToProjectEnvironmentVariableArrayOutput() ProjectEnvironmentVariableArrayOutput {
	return i.ToProjectEnvironmentVariableArrayOutputWithContext(context.Background())
}

func (i ProjectEnvironmentVariableArray) ToProjectEnvironmentVariableArrayOutputWithContext(ctx context.Context) ProjectEnvironmentVariableArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProjectEnvironmentVariableArrayOutput)
}

// ProjectEnvironmentVariableMapInput is an input type that accepts ProjectEnvironmentVariableMap and ProjectEnvironmentVariableMapOutput values.
// You can construct a concrete instance of `ProjectEnvironmentVariableMapInput` via:
//
//	ProjectEnvironmentVariableMap{ "key": ProjectEnvironmentVariableArgs{...} }
type ProjectEnvironmentVariableMapInput interface {
	pulumi.Input

	ToProjectEnvironmentVariableMapOutput() ProjectEnvironmentVariableMapOutput
	ToProjectEnvironmentVariableMapOutputWithContext(context.Context) ProjectEnvironmentVariableMapOutput
}

type ProjectEnvironmentVariableMap map[string]ProjectEnvironmentVariableInput

func (ProjectEnvironmentVariableMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ProjectEnvironmentVariable)(nil)).Elem()
}

func (i ProjectEnvironmentVariableMap) ToProjectEnvironmentVariableMapOutput() ProjectEnvironmentVariableMapOutput {
	return i.ToProjectEnvironmentVariableMapOutputWithContext(context.Background())
}

func (i ProjectEnvironmentVariableMap) ToProjectEnvironmentVariableMapOutputWithContext(ctx context.Context) ProjectEnvironmentVariableMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProjectEnvironmentVariableMapOutput)
}

type ProjectEnvironmentVariableOutput struct{ *pulumi.OutputState }

func (ProjectEnvironmentVariableOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ProjectEnvironmentVariable)(nil)).Elem()
}

func (o ProjectEnvironmentVariableOutput) ToProjectEnvironmentVariableOutput() ProjectEnvironmentVariableOutput {
	return o
}

func (o ProjectEnvironmentVariableOutput) ToProjectEnvironmentVariableOutputWithContext(ctx context.Context) ProjectEnvironmentVariableOutput {
	return o
}

// The git branch of the Environment Variable.
func (o ProjectEnvironmentVariableOutput) GitBranch() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ProjectEnvironmentVariable) pulumi.StringPtrOutput { return v.GitBranch }).(pulumi.StringPtrOutput)
}

// The name of the Environment Variable.
func (o ProjectEnvironmentVariableOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v *ProjectEnvironmentVariable) pulumi.StringOutput { return v.Key }).(pulumi.StringOutput)
}

// The ID of the Vercel project.
func (o ProjectEnvironmentVariableOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v *ProjectEnvironmentVariable) pulumi.StringOutput { return v.ProjectId }).(pulumi.StringOutput)
}

// The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
func (o ProjectEnvironmentVariableOutput) Targets() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *ProjectEnvironmentVariable) pulumi.StringArrayOutput { return v.Targets }).(pulumi.StringArrayOutput)
}

// The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider.
func (o ProjectEnvironmentVariableOutput) TeamId() pulumi.StringOutput {
	return o.ApplyT(func(v *ProjectEnvironmentVariable) pulumi.StringOutput { return v.TeamId }).(pulumi.StringOutput)
}

// The value of the Environment Variable.
func (o ProjectEnvironmentVariableOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v *ProjectEnvironmentVariable) pulumi.StringOutput { return v.Value }).(pulumi.StringOutput)
}

type ProjectEnvironmentVariableArrayOutput struct{ *pulumi.OutputState }

func (ProjectEnvironmentVariableArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ProjectEnvironmentVariable)(nil)).Elem()
}

func (o ProjectEnvironmentVariableArrayOutput) ToProjectEnvironmentVariableArrayOutput() ProjectEnvironmentVariableArrayOutput {
	return o
}

func (o ProjectEnvironmentVariableArrayOutput) ToProjectEnvironmentVariableArrayOutputWithContext(ctx context.Context) ProjectEnvironmentVariableArrayOutput {
	return o
}

func (o ProjectEnvironmentVariableArrayOutput) Index(i pulumi.IntInput) ProjectEnvironmentVariableOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ProjectEnvironmentVariable {
		return vs[0].([]*ProjectEnvironmentVariable)[vs[1].(int)]
	}).(ProjectEnvironmentVariableOutput)
}

type ProjectEnvironmentVariableMapOutput struct{ *pulumi.OutputState }

func (ProjectEnvironmentVariableMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ProjectEnvironmentVariable)(nil)).Elem()
}

func (o ProjectEnvironmentVariableMapOutput) ToProjectEnvironmentVariableMapOutput() ProjectEnvironmentVariableMapOutput {
	return o
}

func (o ProjectEnvironmentVariableMapOutput) ToProjectEnvironmentVariableMapOutputWithContext(ctx context.Context) ProjectEnvironmentVariableMapOutput {
	return o
}

func (o ProjectEnvironmentVariableMapOutput) MapIndex(k pulumi.StringInput) ProjectEnvironmentVariableOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ProjectEnvironmentVariable {
		return vs[0].(map[string]*ProjectEnvironmentVariable)[vs[1].(string)]
	}).(ProjectEnvironmentVariableOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProjectEnvironmentVariableInput)(nil)).Elem(), &ProjectEnvironmentVariable{})
	pulumi.RegisterInputType(reflect.TypeOf((*ProjectEnvironmentVariableArrayInput)(nil)).Elem(), ProjectEnvironmentVariableArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ProjectEnvironmentVariableMapInput)(nil)).Elem(), ProjectEnvironmentVariableMap{})
	pulumi.RegisterOutputType(ProjectEnvironmentVariableOutput{})
	pulumi.RegisterOutputType(ProjectEnvironmentVariableArrayOutput{})
	pulumi.RegisterOutputType(ProjectEnvironmentVariableMapOutput{})
}
