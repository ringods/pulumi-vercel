// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vercel

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-vercel/sdk/go/vercel/internal"
)

func LookupEdgeConfigToken(ctx *pulumi.Context, args *LookupEdgeConfigTokenArgs, opts ...pulumi.InvokeOption) (*LookupEdgeConfigTokenResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupEdgeConfigTokenResult
	err := ctx.Invoke("vercel:index/getEdgeConfigToken:getEdgeConfigToken", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getEdgeConfigToken.
type LookupEdgeConfigTokenArgs struct {
	EdgeConfigId string  `pulumi:"edgeConfigId"`
	TeamId       *string `pulumi:"teamId"`
	Token        string  `pulumi:"token"`
}

// A collection of values returned by getEdgeConfigToken.
type LookupEdgeConfigTokenResult struct {
	ConnectionString string `pulumi:"connectionString"`
	EdgeConfigId     string `pulumi:"edgeConfigId"`
	Id               string `pulumi:"id"`
	Label            string `pulumi:"label"`
	TeamId           string `pulumi:"teamId"`
	Token            string `pulumi:"token"`
}

func LookupEdgeConfigTokenOutput(ctx *pulumi.Context, args LookupEdgeConfigTokenOutputArgs, opts ...pulumi.InvokeOption) LookupEdgeConfigTokenResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupEdgeConfigTokenResultOutput, error) {
			args := v.(LookupEdgeConfigTokenArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv LookupEdgeConfigTokenResult
			secret, err := ctx.InvokePackageRaw("vercel:index/getEdgeConfigToken:getEdgeConfigToken", args, &rv, "", opts...)
			if err != nil {
				return LookupEdgeConfigTokenResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(LookupEdgeConfigTokenResultOutput)
			if secret {
				return pulumi.ToSecret(output).(LookupEdgeConfigTokenResultOutput), nil
			}
			return output, nil
		}).(LookupEdgeConfigTokenResultOutput)
}

// A collection of arguments for invoking getEdgeConfigToken.
type LookupEdgeConfigTokenOutputArgs struct {
	EdgeConfigId pulumi.StringInput    `pulumi:"edgeConfigId"`
	TeamId       pulumi.StringPtrInput `pulumi:"teamId"`
	Token        pulumi.StringInput    `pulumi:"token"`
}

func (LookupEdgeConfigTokenOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupEdgeConfigTokenArgs)(nil)).Elem()
}

// A collection of values returned by getEdgeConfigToken.
type LookupEdgeConfigTokenResultOutput struct{ *pulumi.OutputState }

func (LookupEdgeConfigTokenResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupEdgeConfigTokenResult)(nil)).Elem()
}

func (o LookupEdgeConfigTokenResultOutput) ToLookupEdgeConfigTokenResultOutput() LookupEdgeConfigTokenResultOutput {
	return o
}

func (o LookupEdgeConfigTokenResultOutput) ToLookupEdgeConfigTokenResultOutputWithContext(ctx context.Context) LookupEdgeConfigTokenResultOutput {
	return o
}

func (o LookupEdgeConfigTokenResultOutput) ConnectionString() pulumi.StringOutput {
	return o.ApplyT(func(v LookupEdgeConfigTokenResult) string { return v.ConnectionString }).(pulumi.StringOutput)
}

func (o LookupEdgeConfigTokenResultOutput) EdgeConfigId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupEdgeConfigTokenResult) string { return v.EdgeConfigId }).(pulumi.StringOutput)
}

func (o LookupEdgeConfigTokenResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupEdgeConfigTokenResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupEdgeConfigTokenResultOutput) Label() pulumi.StringOutput {
	return o.ApplyT(func(v LookupEdgeConfigTokenResult) string { return v.Label }).(pulumi.StringOutput)
}

func (o LookupEdgeConfigTokenResultOutput) TeamId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupEdgeConfigTokenResult) string { return v.TeamId }).(pulumi.StringOutput)
}

func (o LookupEdgeConfigTokenResultOutput) Token() pulumi.StringOutput {
	return o.ApplyT(func(v LookupEdgeConfigTokenResult) string { return v.Token }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupEdgeConfigTokenResultOutput{})
}
