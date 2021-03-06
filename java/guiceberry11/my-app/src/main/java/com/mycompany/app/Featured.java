// package tutorial_1_server.prod;
package com.mycompany.app;

import static java.lang.annotation.ElementType.FIELD;
import static java.lang.annotation.ElementType.METHOD;
import static java.lang.annotation.ElementType.PARAMETER;
import static java.lang.annotation.RetentionPolicy.RUNTIME;

import com.google.inject.BindingAnnotation;

import java.lang.annotation.Retention;
import java.lang.annotation.Target;

/**
 * Denotes which {@link Pet} is to be featured today.
 */
@Retention(RUNTIME) 
@Target({FIELD, METHOD, PARAMETER}) 
@BindingAnnotation
public @interface Featured {}
